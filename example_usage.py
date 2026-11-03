"""
Example Usage: Muscle Mechanomyography (MMG) & Contractile Stiffness Evaluation.
Demonstrates acoustic myography analysis and electromechanical delay measurement.
"""

from client import MuscleMechanomyographyClient


def main():
    client = MuscleMechanomyographyClient()
    print("=== Muscle Mechanomyography (MMG) Dynamics Demo ===")

    # Test Case 1: Healthy rested skeletal muscle
    res1 = client.evaluate_mechanomyography(
        mmg_rms_amplitude_mv=1.92,
        mmg_mean_power_frequency_hz=27.4,
        electromechanical_delay_ms=33.5,
        muscle_stiffness_n_m=275.0
    )
    print("\nTest Case 1: Rested Skeletal Muscle (Vastus Lateralis)")
    print(f"  MMG RMS: {res1['mmg_rms_amplitude_mv']} mV | MPF: {res1['mmg_mean_power_frequency_hz']} Hz")
    print(f"  Electromechanical Delay (EMD): {res1['electromechanical_delay_ms']} ms")
    print(f"  Mechanical Coupling Index: {res1['neuromuscular_mechanical_coupling_index']}")
    print(f"  Contractile Score: {res1['muscular_contractile_score']} / 100")
    print(f"  Classification: {res1['classification']}")
    print(f"  Guidance: {res1['actionable_guidance']}")

    # Test Case 2: Fatigued muscle after sustained isometric contraction
    res2 = client.evaluate_mechanomyography(
        mmg_rms_amplitude_mv=2.85,
        mmg_mean_power_frequency_hz=14.2,
        electromechanical_delay_ms=64.0
    )
    print("\nTest Case 2: Muscular Fatigue & Excitation Delay")
    print(f"  MMG RMS: {res2['mmg_rms_amplitude_mv']} mV | MPF: {res2['mmg_mean_power_frequency_hz']} Hz")
    print(f"  EMD: {res2['electromechanical_delay_ms']} ms")
    print(f"  Contractile Score: {res2['muscular_contractile_score']} / 100")
    print(f"  Classification: {res2['classification']}")
    print(f"  Guidance: {res2['actionable_guidance']}")


if __name__ == "__main__":
    main()
