from __future__ import annotations

"""Engine 4 production entrypoint with SSOT v4.7 live-trigger guard."""

import engine4_pipeline as core
import engine4_pipeline_runner as base
from engine4_final_guard import guarded_final_stage


def main() -> None:
    # Install the verified free-provider repairs first, then replace only the final
    # signal function with the live-price trigger guard required by SSOT v4.7.
    base.install_repairs()
    core.final_stage = guarded_final_stage
    base.main()


if __name__ == "__main__":
    main()
