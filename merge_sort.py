merge = []
for i in range(8):
    num = int(input("Number: "))
    merge.append(num)


def merge_sort(m):
    if len(m) == 1:
        print(m)
        return m
    print(m)
    sorted_list = []
    m_lower = merge_sort(m[:len(m)//2])
    m_upper = merge_sort(m[len(m)//2:])
    for i in range(len(m_lower)+len(m_upper)):
        if len(m_lower) == 0:
            for element in m_upper:
                sorted_list.append(element)
            break
        if len(m_upper) == 0:
            for element in m_lower:
                sorted_list.append(element)
            break
        if m_lower[0] < m_upper[0]:
            sorted_list.append(m_lower[0])
            m_lower.pop(0)
        else:
            sorted_list.append(m_upper[0])
            m_upper.pop(0)
    print(f"sorted list {sorted_list}")
    return sorted_list


print(merge_sort(merge))

