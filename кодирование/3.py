import math

for m_v in range(1, 1000):
    m_p = 4 * m_v
    petya = m_p * 16 + 1000 * math.ceil(math.log(m_p, 2))
    vasya = m_v * 16 + 1000 * math.ceil(math.log(m_v, 2))
    if petya - vasya == 640 * 8:
        print(vasya // 8)