# Towards Formal Verification of State Continuity for Enclave Programs

This repo contains [Tamarin](https://tamarin-prover.github.io/) models for [Intel SGX](https://software.intel.com/content/www/us/en/develop/topics/software-guard-extensions.html) application components of three open source projects: [Hyperledger Sawtooth](https://www.hyperledger.org/use/sawtooth), [SGXEnabledAccess](https://github.com/fishermano/SGXEnabledAccess), [BI-SGX](https://bi-sgx.net/). These models can be helpful to verify the properties of any other SGX application. Each model uses many SGX primitives, some of which are directly reusable. Other primitive requires customized integration as per application requirement. Details of the three open-source projects, the SGX threat model, the working principles behind the SGX primitives are described in our paper (TBD).

## File structure of this repo

1. Tamarin codes files for each case study of our paper are in 3 separate folders – Sawtooth, SGXEnabledAccess, BI-SGX. Each of these folders contains two sub-folders: safe and vulnerable, which contain the safe and vulnerable Tamarin model files respectively.
2. The Tamarin model files are with extension *.spthy; Tamarin proof output is saved with* .proof files; the attack trace images are saved with file names trace_*.png for vulnerable models.

## Proofs

1. The proofs were run with Tamarin prover (v1.7.0) on a machine with a quad-core 1.80GHz Intel© Core i7-8550U CPU and 16 GB RAM, and Ubuntu Linux 18.04. Proof of SGXEnabledAccess also requires python3 installation. Tamarin (v1.7.0) can be installed from the [Tamarin GitHub repo](https://github.com/tamarin-prover/tamarin-prover).
2. For each Tamarin model, the Tamarin heuristics and trace algorithm parameters are specified in the model files as comments.

## Model Primitives used in our work

### SGX primitives

1. Enclave call (ecall) threads
2. Association Network of SGX entities (ISV, Remote Users, SGX machines (platforms), enclave-binary, enclave-processes, owner specific identities for key derivation and monotonic counters)
3. Monotonic Counters
4. Local/Global variables
5. SGX threat model (Table 1 in the paper)
6. Key Derivation
7. Sealing

### Programming primitives

1. Locks
2. Loops and Branching
3. Database (Read only)
4. Random number Input 

Out of the above primitives monotonic counters, locks, local/global variables, and the programming primitives can be reused directly. Other require manual integration based on the code component under consideration.     

Sawtooth uses all the SGX primitives with single threaded ecalls.

SGXEnabledAccess uses multi-threaded ecalls, local/global variables, SGX threat model, key derivation, locks, loops, and branching

BI-SGX uses single threaded ecalls and all the primitives except Loops and Branching.

## Process of SGX application formal verification using Tamarin prover.

1. [Install](https://tamarin-prover.github.io/manual/book/002_installation.html) Tamarin prover and learn how to use it from the [Tamarin Manual](https://tamarin-prover.github.io/manual/tex/tamarin-manual.pdf), [Tamarin code examples](https://github.com/tamarin-prover/tamarin-prover/tree/develop/examples), [other research works](https://tamarin-prover.github.io/), [Exercise at VeryCrypto](https://github.com/aseemr/Indocrypt-VerifiedCrypto-Tutorials/blob/main/Tamarin/exercise_starter.md), [Exercise](https://github.com/benjaminkiesl/tamarin_toy_protocol) by Dr. Kiesl, Tutorials [Blog](https://hajji.org/en/crypto/verified-crypto/tamarin) [Video](https://youtu.be/XptJG19hDcQ)  
2. Identify the control flow of your SGX application’s code component and the desired properties that you hope to verify.
3. Identify the code variables, trusted and untrusted boundaries, and the SGX primitives required to build the formal model of the code component. Explore the models in this repo to find what primitives can you reproduced for your model.
4. Start with a simple model and ensure correct syntax and protocol behavior using [executability lemmas](https://tamarin-prover.github.io/manual/tex/tamarin-manual.pdf)
5. Write properties in First-Order Logic; Get Initial results; validate the trace result into application code if possible; gradually add other functionalities, and repeat the process. If you encounter non-termination, see the section below. 

## Potential approaches to resolve non-termination

1. Run Tamarin Interactive GUI without `--prove` flag. Observe if all the [partial deconstructions](https://tamarin-prover.github.io/manual/book/008_precomputation.html) are resolved. if not the [Auto-Source paper](https://hal.archives-ouvertes.fr/hal-02903620/document) and the [TLS1.3 thesis](https://pure.royalholloway.ac.uk/portal/files/33074422/2018HoylandJGPhD.pdf) can help.  
2. Try all Tamarin binary parameters `--stop-on-trace` and `--heuristic` to see if any combination terminates the proof in a reasonable time (learned by experience; this can vary for different model sizes and complexity). [UT Tamarin](https://github.com/benjaminkiesl/ut_tamarin) could be useful here.  
3. Try [induction lemmas](https://tamarin-prover.github.io/manual/book/010_advanced-features.html)
4. Try to minimize looped fact dependencies. An example could be found [here](https://groups.google.com/g/tamarin-prover/c/XAf-mO86d2Y). The looped dependencies could be complex — "Another source of non-termination that is a feature of Tamarin's unrolling is interacting inductive lemmas. You can create pathological examples where you have loops that are not well-bracketed, i.e. the loops partially overlap, something like `[(])` where `[]` and `()` are looping states. If you have one inductive lemma for each loop you may not be able to solve either one. The only times I've ever run into this in practice is when I've tried to decompose inductive lemmas too far to try and make the automated prover solve more." noted by Jonathan Hoyland 
5. Try following methods     
    1. Manually reason about why the property you expect should hold in the model
    2. Observe the proof steps in [Tamarin interactive GUI](https://tamarin-prover.github.io/manual/book/003_example.html) and identify the pattern of the proof or observe if the proof process is resolving a set of similar constraint repeatedly

    Based on the above methods build [helper lemmas](https://tamarin-prover.github.io/manual/book/010_advanced-features.html) or customized heuristic using [an oracle script](https://tamarin-prover.github.io/manual/book/010_advanced-features.html)       

6. Xor equation theory and Rule variants -- An adversary can not rule out the possibility of Fr(a) from one rule to be the same as Fr(b) from another rule. — [google group chat](https://groups.google.com/g/tamarin-prover/c/irq09b70WS8)
7. Go through [Tamarin Google Forum](https://groups.google.com/g/tamarin-prover) and ask for help. The forum history contains many modeling tips and tricks. 
8. Also, note that proving a property for a given model is undecidable. Therefore, it is impossible to ensure termination in all cases.

## Remarks about Formal Modeling

1. [SoK: Computer-Aided Cryptography](https://eprint.iacr.org/2019/1393.pdf) — describes the state of Formal Methods in a broader perspective.  
2. The equivalence of an application code and the constructed model is made by the best human effort (without proof). Therefore, verification results for any constructed model convey knowledge about the model rather than the application code that it represents. In my opinion, this approximation (aka verification gap) is not a big barrier to the utility of formal verification because verification results: especially flaws can be double-checked back in the application code. Moreover, proving the property of an approximate model serves the purpose of formal verification well enough in many real-world cases. 
3. It is very important to understand the assumptions of the model. "A proof is only as good as its model" ([source](https://pure.royalholloway.ac.uk/portal/files/33074422/2018HoylandJGPhD.pdf), page 43)

## Acknowledgment

We thank Cas Cremers, Jonathan Hoyland, Benjamin Kiesl, Jannik Dreier, Kevin Milner and Tamarin community at the Google forum for providing insight into Tamarin and for active support and suggestions during our research process.