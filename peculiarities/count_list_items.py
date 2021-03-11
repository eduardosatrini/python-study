# Count how many times each item appears in the list
m_list = [
    'a', 'b', 'd', 'h', 'v',
    'b', 'a', 'a', 'i', 'd'
]

print(m_list)

for item in sorted(set(m_list)):
    c = m_list.count(item)
    print(f"{item} = {c} times.")
