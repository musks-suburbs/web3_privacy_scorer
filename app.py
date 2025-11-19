#!/usr/bin/env python3
import argparse
from dataclasses import dataclass, asdict
from typing import Dict, Any


@dataclass
class PrivacyProfile:
    name: str
    description: str
    uses_zk: bool
    uses_fhe: bool
    open_source: bool
    audited: bool
    soundness_focus: bool


PROFILES: Dict[str, PrivacyProfile] = {
    "aztec": PrivacyProfile(
        name="Aztec-like L2",
        description="Inspired by Aztec: zk rollup with privacy-preserving smart contracts.",
        uses_zk=True,
        uses_fhe=False,
        open_source=True,
        audited=True,
        soundness_focus=True,
    ),
    "zama": PrivacyProfile(
        name="Zama-like FHE stack",
        description="Inspired by Zama: fully homomorphic encryption for Web3 and cryptography.",
        uses_zk=False,
        uses_fhe=True,
        open_source=True,
        audited=False,
        soundness_focus=True,
    ),
    "soundness": PrivacyProfile(
        name="Soundness-focused lab",
        description="Inspired by soundness research labs: formal verification and proofs first.",
        uses_zk=True,
        uses_fhe=False,
        open_source=False,
        audited=True,
        soundness_focus=True,
    ),
}


def score_profile(profile: PrivacyProfile) -> int:
    score = 0
    if profile.uses_zk:
        score += 30
    if profile.uses_fhe:
        score += 30
    if profile.open_source:
        score += 15
    if profile.audited:
        score += 15
    if profile.soundness_focus:
        score += 10
    return min(score, 100)


def summarize_profile(profile: PrivacyProfile) -> str:
    score = score_profile(profile)
    flags = []
    flags.append(f"Uses zero-knowledge proofs: {'yes' if profile.uses_zk else 'no'}")
    flags.append(f"Uses fully homomorphic encryption: {'yes' if profile.uses_fhe else 'no'}")
    flags.append(f"Open source code: {'yes' if profile.open_source else 'no'}")
    flags.append(f"External audits: {'yes' if profile.audited else 'no'}")
    flags.append(f"Formal soundness focus: {'yes' if profile.soundness_focus else 'no'}")

    lines = []
    lines.append(f"Name: {profile.name}")
    lines.append(f"Description: {profile.description}")
    lines.append("")
    lines.append("Features:")
    for f in flags:
        lines.append(f"  - {f}")
    lines.append("")
    lines.append(f"Estimated privacy-strength score: {score}/100")
    lines.append("")
    lines.append("Note: This score is a toy heuristic for educational purposes only.")
    lines.append("Always rely on official audits, specifications, and documentation.")
    return "\n".join(lines)


def profile_from_args(args: argparse.Namespace) -> PrivacyProfile:
    # Build a profile from flags. Defaults assume a basic Web3 project.
    return PrivacyProfile(
        name=args.name or "Custom Web3 project",
        description=args.description or "User-defined Web3 project privacy profile.",
        uses_zk=args.zk,
        uses_fhe=args.fhe,
        open_source=args.open_source,
        audited=args.audited,
        soundness_focus=args.soundness,
    )


def list_profiles() -> None:
    print("Built-in example profiles related to Web3 privacy and soundness:")
    for key, profile in PROFILES.items():
        print(f"- {key}: {profile.name}")


def export_json(profile: PrivacyProfile) -> str:
    # Low-tech JSON export without importing json to keep the script simple and self-contained.
    data: Dict[str, Any] = asdict(profile)
    data["score"] = score_profile(profile)
    parts = ["{"]
    for i, (k, v) in enumerate(data.items()):
        if isinstance(v, bool):
            val = "true" if v else "false"
        elif isinstance(v, int):
            val = str(v)
        else:
            val = '"' + str(v).replace('"', '\\"') + '"'
        comma = "," if i < len(data) - 1 else ""
        parts.append(f'  "{k}": {val}{comma}')
    parts.append("}")
    return "\n".join(parts)


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "web3_privacy_scorer: small CLI to estimate a toy privacy score "
            "for Web3-style projects, inspired by ecosystems like Aztec, Zama, "
            "and soundness-focused research labs."
        )
    )

    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--profile",
        type=str,
        help="Use a built-in profile (aztec, zama, soundness).",
    )
    group.add_argument(
        "--custom",
        action="store_true",
        help="Define a custom project profile using flags.",
    )

    parser.add_argument("--name", type=str, help="Name of the custom project.")
    parser.add_argument("--description", type=str, help="Description of the custom project.")

    parser.add_argument("--zk", action="store_true", help="Project uses zero-knowledge proofs.")
    parser.add_argument("--fhe", action="store_true", help="Project uses fully homomorphic encryption.")
    parser.add_argument("--open-source", action="store_true", help="Project is open source.")
    parser.add_argument("--audited", action="store_true", help="Project has external audits.")
    parser.add_argument("--soundness", action="store_true", help="Strong focus on formal soundness and verification.")

    parser.add_argument(
        "--list-profiles",
        action="store_true",
        help="List built-in example profiles.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Print result as a minimal JSON object instead of human-readable text.",
    )

    args = parser.parse_args()

    if args.list_profiles:
        list_profiles()
        return

    if args.profile:
        key = args.profile.lower()
        if key not in PROFILES:
            print("Unknown profile key. Available options:")
            list_profiles()
            return
        profile = PROFILES[key]
    else:
        profile = profile_from_args(args)

    if args.json:
        print(export_json(profile))
    else:
        print(summarize_profile(profile))


if __name__ == "__main__":
    main()
