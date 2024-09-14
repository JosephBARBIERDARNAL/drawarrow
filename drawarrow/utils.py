import math


def _calculate_angles(pos_A, pos_B, pos_C):

    def magnitude(v):
        return math.sqrt(v[0] ** 2 + v[1] ** 2)

    def dot_product(v1, v2):
        return v1[0] * v2[0] + v1[1] * v2[1]

    def angle_with_x_axis(v):
        return math.degrees(math.atan2(v[1], v[0]))

    AB = (pos_B[0] - pos_A[0], pos_B[1] - pos_A[1])
    BC = (pos_C[0] - pos_B[0], pos_C[1] - pos_B[1])

    magnitude_AB = magnitude(AB)
    magnitude_BC = magnitude(BC)

    dot_AB_BC = dot_product(AB, BC)

    cos_theta = dot_AB_BC / (magnitude_AB * magnitude_BC)

    cos_theta = max(-1, min(1, cos_theta))

    angle_between_AB_BC = math.degrees(math.acos(cos_theta))

    angleA = angle_with_x_axis(AB)
    angleB = angle_with_x_axis(BC)

    # print(angleA, angleB)
    return angleA, angleB


if __name__ == "__main__":

    pos_A = (1, 1)
    pos_B = (2, 2)
    pos_C = (3, 1)

    angle_AB, angle_BC = _calculate_angles(pos_A, pos_B, pos_C)
    print(f"Angle between pos_A and pos_B: {angle_AB:.2f} degrees")
    print(f"Angle between pos_B and pos_C: {angle_BC:.2f} degrees")
