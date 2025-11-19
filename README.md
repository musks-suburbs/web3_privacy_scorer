# web3_privacy_scorer

This repository contains a small command-line tool that estimates a toy privacy and soundness score for Web3-style projects. It is inspired by domains such as Aztec style zero-knowledge rollups, Zama style fully homomorphic encryption stacks, and research labs focused on protocol soundness.

The repository must contain exactly two files.

1. app.py  
2. README.md  


## Purpose

The script helps you quickly sketch how strong the privacy posture of a project might look under a simple heuristic. It does not perform any blockchain calls and does not contact external APIs. The goal is to provide an offline educational utility that encourages thinking in terms of zero knowledge, fully homomorphic encryption, open source practices, audits, and soundness focused verification.


## How it works

The tool works with two kinds of profiles.

1. Built in profiles  
   These are example configurations inspired by real ecosystems.

   aztec  
   Represents a privacy oriented layer two rollup using zero knowledge proofs and private smart contracts.

   zama  
   Represents a stack where fully homomorphic encryption is a primary building block for computing over encrypted data.

   soundness  
   Represents a research or engineering group that puts formal correctness, proofs, and protocol soundness at the center.

2. Custom profiles  
   You can define your own project by combining boolean flags about the technologies and practices it uses.


## Scoring model

The script computes a score between 0 and 100. The score is not meant to be scientific. It is only a learning tool.

Rough scoring idea:

uses zero knowledge proofs adds up to 30 points  
uses fully homomorphic encryption adds up to 30 points  
open source adds up to 15 points  
external audits add up to 15 points  
soundness focused development adds up to 10 points  

The exact values are encoded inside the app.py file. The score is always capped at 100.


## Installation

Requirements:

Python 3.10 or newer must be installed and available on your PATH.  
Any operating system with a command line shell will work.

Steps:

1. Create a new GitHub repository with any name you like.  
2. Place app.py and this README.md file into the root of the repository.  
3. Optionally run python app.py with no flags to see a short description in the help text that argparse provides.  
4. No extra packages are required beyond the Python standard library.


## Usage examples

Run from the root folder of your clone.

List built in profiles:

python app.py --list-profiles

Use the Aztec inspired profile and see a human readable report:

python app.py --profile aztec

Use the Zama inspired profile and get a compact JSON view:

python app.py --profile zama --json

Use a soundness inspired profile:

python app.py --profile soundness

Define a custom project that uses zero knowledge proofs, has external audits, and is open source:

python app.py --custom --name MyZkApp --zk --audited --open-source

Define a hypothetical project that uses both zero knowledge proofs and fully homomorphic encryption and is very soundness focused:

python app.py --custom --name HybridZkFheLab --zk --fhe --soundness --open-source --audited


## Expected output

For human readable mode the tool prints:

name of the profile  
a short description  
a list of key features and which of them are enabled  
the estimated score out of 100  
a reminder that this is only a toy model

For JSON mode the tool prints a small JSON object with the fields:

name  
description  
uses_zk  
uses_fhe  
open_source  
audited  
soundness_focus  
score  


## Notes and limitations

The project is intentionally minimal and focused on core ideas from Web3 privacy ecosystems such as Aztec, Zama and soundness oriented research. It does not claim to be an accurate risk or security assessment framework. For any real world protocol, always rely on formal audits, peer reviewed research, and official documentation.

You are encouraged to fork the repository and adjust the scoring rules, add more profiles, or integrate this script into a broader toolchain for documenting or teaching privacy properties of decentralized systems.
