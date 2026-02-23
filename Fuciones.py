import math

# =========================
# OIL & GAS / PETROLEUM
# =========================

def api_gravity(sg_oil):
    """
    API gravity from specific gravity (SG) at 60°F.
    API = (141.5 / SG) - 131.5
    """
    if sg_oil <= 0:
        raise ValueError("sg_oil must be > 0")
    return (141.5 / sg_oil) - 131.5


def gor_from_rates(q_gas_scf_d, q_oil_stb_d):
    """
    Gas-Oil Ratio (GOR) in scf/STB.
    """
    if q_oil_stb_d <= 0:
        raise ValueError("q_oil_stb_d must be > 0")
    return q_gas_scf_d / q_oil_stb_d


def darcy_flow_rate(k_md, area_ft2, dp_psi, mu_cp, length_ft, b_o=1.0):
    """
    Darcy’s law (field-unit style) - rough engineering calc.
    q (STB/d) ≈ 0.001127 * k(md) * A(ft2) * ΔP(psi) / (μ(cp) * L(ft)) / B
    """
    if mu_cp <= 0 or length_ft <= 0 or b_o <= 0:
        raise ValueError("mu_cp, length_ft, b_o must be > 0")
    return 0.001127 * k_md * area_ft2 * dp_psi / (mu_cp * length_ft) / b_o


# =========================
# ENERGY / ELECTRICAL
# =========================

def three_phase_power_kw(v_ll, current_a, power_factor=0.9):
    """
    3-phase active power:
    P(kW) = sqrt(3) * V_line-line * I * PF / 1000
    """
    if v_ll < 0 or current_a < 0:
        raise ValueError("v_ll and current_a must be >= 0")
    if not (0 <= power_factor <= 1):
        raise ValueError("power_factor must be between 0 and 1")
    return (math.sqrt(3) * v_ll * current_a * power_factor) / 1000


def motor_efficiency(output_kw, input_kw):
    """
    Efficiency = output / input (0..1)
    """
    if input_kw <= 0:
        raise ValueError("input_kw must be > 0")
    return output_kw / input_kw


# =========================
# FINANCE
# =========================

def npv(discount_rate, cashflows):
    """
    Net Present Value.
    discount_rate: decimal (e.g., 0.12)
    cashflows: list/tuple like [CF0, CF1, CF2, ...]
    """
    if discount_rate <= -1:
        raise ValueError("discount_rate must be > -1")
    return sum(cf / ((1 + discount_rate) ** t) for t, cf in enumerate(cashflows))


def roi(gain, cost):
    """
    ROI = (gain - cost) / cost
    """
    if cost == 0:
        raise ValueError("cost must be non-zero")
    return (gain - cost) / cost


# =========================
# OPERATIONS / QUALITY
# =========================

def oee(availability, performance, quality):
    """
    OEE = Availability * Performance * Quality
    Inputs in decimals (0..1)
    """
    for x in (availability, performance, quality):
        if not (0 <= x <= 1):
            raise ValueError("availability, performance, quality must be between 0 and 1")
    return availability * performance * quality


def defect_rate(defects, total_units):
    """
    Defect rate = defects / total_units
    """
    if total_units <= 0:
        raise ValueError("total_units must be > 0")
    if defects < 0:
        raise ValueError("defects must be >= 0")
    return defects / total_units


# =========================
# DATA / ANALYTICS (GENERIC)
# =========================

def z_score(x, mean, std):
    """
    Z-score = (x - mean) / std
    """
    if std <= 0:
        raise ValueError("std must be > 0")
    return (x - mean) / std


def exponential_smoothing(prev_forecast, actual, alpha=0.3):
    """
    Simple Exponential Smoothing:
    F_t = alpha * A_{t-1} + (1-alpha) * F_{t-1}
    """
    if not (0 < alpha <= 1):
        raise ValueError("alpha must be in (0, 1]")
    return alpha * actual + (1 - alpha) * prev_forecast

def interes_simple(capital_inicial=0, tiempo_meses=1, tasa_interes = 0.05):
    """
    Función para calcular el interés simple
    Parámetros:
    capital_inicial: Capital inicial en soles S/
    tiempo_meses: Tiempo en meses en valor entero
    tasa_interes: Tasa de interés en decimales
    return: Retorna el interés simple en soles S/
    """
    interes = capital_inicial * tasa_interes * (tiempo_meses/12)
    return interes