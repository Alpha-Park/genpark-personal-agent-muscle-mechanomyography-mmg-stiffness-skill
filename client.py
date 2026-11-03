"""
Muscle Mechanomyography (MMG) & Contractile Stiffness Engine.
Provides deterministic, zero-dependency modeling of mechanomyographic RMS amplitude,
mean power frequency (MPF), electromechanical delay (EMD), and skeletal muscle fatigue kinetics.
"""

from typing import Dict, Any, List, Optional


class MuscleMechanomyographyClient:
    """
    Deterministic client for analyzing Muscle Mechanomyography (MMG) / Acoustic Myography.
    Measures transverse low-frequency mechanical vibrations of contracting skeletal muscle fibers,
    quantifying motor unit recruitment, firing rate dynamics, and peripheral muscular fatigue.
    """

    def __init__(self):
        pass

    def evaluate_mechanomyography(
        self,
        mmg_rms_amplitude_mv: float,
        mmg_mean_power_frequency_hz: float,
        electromechanical_delay_ms: float,
        muscle_stiffness_n_m: Optional[float] = None
    ) -> Dict[str, Any]:
        """
        Evaluates neuromuscular MMG parameters:
        - MMG RMS: gross motor unit mechanical recruitment
        - MMG MPF: motor unit discharge rate (normal 15 - 35 Hz)
        - Electromechanical Delay (EMD): excitation-contraction coupling latency (normal 25 - 55 ms)
        """
        if mmg_rms_amplitude_mv <= 0 or mmg_mean_power_frequency_hz <= 0 or electromechanical_delay_ms <= 0:
            return {"error": "Invalid inputs: RMS, MPF, and EMD must be positive values"}

        # Neuromuscular Mechanical Coupling Index (NMCI):
        # High MPF with low EMD signifies crisp cross-bridge cycling
        nmci = round((mmg_mean_power_frequency_hz / electromechanical_delay_ms) * 100.0, 1)

        # Muscular Contractile Dynamic Score (0 - 100):
        # Target EMD 28-45 ms, MPF 20-32 Hz -> 85-95.
        # EMD > 60 ms or MPF < 14 Hz -> < 50 (Peripheral fatigue / excitation-contraction uncoupling).
        score = 80.0
        if 25.0 <= electromechanical_delay_ms <= 45.0:
            score += 10.0
        elif electromechanical_delay_ms > 60.0:
            score -= 25.0
        elif electromechanical_delay_ms > 50.0:
            score -= 10.0

        if 20.0 <= mmg_mean_power_frequency_hz <= 34.0:
            score += 10.0
        elif mmg_mean_power_frequency_hz < 15.0:
            score -= 20.0

        final_score = round(min(100.0, max(5.0, score)), 1)

        if final_score >= 85.0:
            tier = "OPTIMAL_CONTRACTILE_EFFICIENCY"
            interp = f"Rapid electromechanical transmission (EMD {electromechanical_delay_ms} ms, MPF {mmg_mean_power_frequency_hz} Hz); high cross-bridge kinetics."
            guidance = "Muscular contraction dynamics are crisp. Ideal capacity for explosive or sustained ergonomic exertion."
        elif final_score >= 70.0:
            tier = "NORMAL_NEUROMUSCULAR_MECHANICS"
            interp = f"Preserved mechanical vibrational response (EMD {electromechanical_delay_ms} ms, NMCI {nmci}); normal motor unit recruitment."
            guidance = "Normal neuromuscular status. Follow scheduled stretching and periodic postural adjustments."
        elif electromechanical_delay_ms > 55.0 or mmg_mean_power_frequency_hz < 16.0:
            tier = "PERIPHERAL_FATIGUE_EXCITATION_DELAY"
            interp = f"Elongated electromechanical delay ({electromechanical_delay_ms} ms) and reduced firing rate; reflects intracellular Ca2+ release slowing or metabolic fatigue."
            guidance = "Peripheral muscular fatigue detected. Incorporate targeted decompression, active recovery, and magnesium/hydration support."
        else:
            tier = "REDUCED_MECHANICAL_COMPLIANCE"
            interp = f"Suboptimal vibrational frequency profile (NMCI {nmci}); elevated stiffness or localized myofascial tension."
            guidance = "Elevated muscular stiffness. Perform mobility drills and light myofascial release."

        return {
            "mmg_rms_amplitude_mv": mmg_rms_amplitude_mv,
            "mmg_mean_power_frequency_hz": mmg_mean_power_frequency_hz,
            "electromechanical_delay_ms": electromechanical_delay_ms,
            "muscle_stiffness_n_m": muscle_stiffness_n_m,
            "neuromuscular_mechanical_coupling_index": nmci,
            "muscular_contractile_score": final_score,
            "classification": tier,
            "physiological_interpretation": interp,
            "actionable_guidance": guidance
        }
