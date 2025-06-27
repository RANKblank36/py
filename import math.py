import math

def trig_calculator():
    try:

        angle_deg = float(input("Enter angle in degrees: "))

        angle_rad = math.radians(angle_deg)

        sin_val = math.sin(angle_rad)
        cos_val = math.cos(angle_rad)
        tan_val = math.tan(angle_rad)

        print(f"\n📐 Trigonometric values for {angle_deg}°:")
        print(f"Sine    (sin): {sin_val:.4f}")
        print(f"Cosine  (cos): {cos_val:.4f}")
        print(f"Tangent (tan): {tan_val:.4f}")

    except ValueError:
        print("Oops! Please enter a valid number.")

trig_calculator()
