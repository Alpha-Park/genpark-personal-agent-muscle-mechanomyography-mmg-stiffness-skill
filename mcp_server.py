"""
MCP Server for Muscle Mechanomyography (MMG) & Stiffness Skill.
Exposes JSON-RPC Model Context Protocol tools for analyzing acoustic myography, electromechanical delay, and peripheral muscular fatigue.
"""

import sys
import json
from typing import Dict, Any
from client import MuscleMechanomyographyClient


def get_tools_manifest() -> Dict[str, Any]:
    return {
        "tools": [
            {
                "name": "evaluate_mechanomyography",
                "description": "Calculates muscle mechanomyography (MMG) parameters: RMS amplitude, mean power frequency, electromechanical delay (EMD), and muscular contractile score.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "mmg_rms_amplitude_mv": {
                            "type": "number",
                            "description": "Root-mean-square amplitude of transverse muscular vibration in mV (e.g. 1.85 mV)."
                        },
                        "mmg_mean_power_frequency_hz": {
                            "type": "number",
                            "description": "Mean power frequency of mechanomyogram in Hz (e.g. 26.5 Hz)."
                        },
                        "electromechanical_delay_ms": {
                            "type": "number",
                            "description": "Excitation-contraction delay between EMG onset and mechanical MMG onset in ms (e.g. 36.0 ms)."
                        },
                        "muscle_stiffness_n_m": {
                            "type": "number",
                            "description": "Optional transverse muscle stiffness in N/m (e.g. 285.0 N/m)."
                        }
                    },
                    "required": [
                        "mmg_rms_amplitude_mv",
                        "mmg_mean_power_frequency_hz",
                        "electromechanical_delay_ms"
                    ]
                }
            }
        ]
    }


def handle_request(client: MuscleMechanomyographyClient, req: Dict[str, Any]) -> Dict[str, Any]:
    method = req.get("method")
    params = req.get("params", {})
    req_id = req.get("id")

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": get_tools_manifest()
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})

        if name == "evaluate_mechanomyography":
            stiff_val = args.get("muscle_stiffness_n_m")
            if stiff_val is not None:
                stiff_val = float(stiff_val)

            res = client.evaluate_mechanomyography(
                mmg_rms_amplitude_mv=float(args.get("mmg_rms_amplitude_mv", 1.8)),
                mmg_mean_power_frequency_hz=float(args.get("mmg_mean_power_frequency_hz", 25.0)),
                electromechanical_delay_ms=float(args.get("electromechanical_delay_ms", 35.0)),
                muscle_stiffness_n_m=stiff_val
            )
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps(res, indent=2)
                        }
                    ]
                }
            }
        else:
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "error": {
                    "code": -32601,
                    "message": f"Method {name} not found"
                }
            }
    else:
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "error": {
                "code": -32600,
                "message": "Invalid request"
            }
        }


def main():
    client = MuscleMechanomyographyClient()
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            resp = handle_request(client, req)
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        except Exception as e:
            err_resp = {
                "jsonrpc": "2.0",
                "id": None,
                "error": {"code": -32700, "message": str(e)}
            }
            sys.stdout.write(json.dumps(err_resp) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
