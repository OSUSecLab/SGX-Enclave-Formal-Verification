Towards Formal Verification of State Continuity for Enclave Programs 
==============================================================================

We model state continuity components of three open source projects [Hyperledger Sawtooth](https://www.hyperledger.org/use/sawtooth), [SGXEnabledAccess](https://github.com/fishermano/SGXEnabledAccess), [BI-SGX](https://bi-sgx.net/). 

Notes:
-------------------

1. Tamarin codes files for each case study of our paper are in 3 separate folders --  Sawtooth, SGXEnabledAccess, BI-SGX. Each of these folders contains two sub-folders: safe and vulnerable, which contain the safe and vulnerable Tamarin model files respectively.

2. The Tamarin model files are with extension *.spthy; Tamarin proof output is saved with *.proof files; the attack trace images are saved with file names trace_*.png for vulnerable models.    

4. Tamarin (v1.7.0) can be installed from GitHub repo https://github.com/tamarin-prover/tamarin-prover. One of the proof also requires python3 installation.  

3. The proofs were run with Tamarin prover (v1.7.0) on a machine with a quad-core 1.80GHz Intel© Core™ i7-8550U CPU and 16 GB RAM, and Ubuntu Linux 18.04. 

5. For each Tamarin model, the Tamarin heuristics and trace algorithm parameters are specified in the model files as comments.
