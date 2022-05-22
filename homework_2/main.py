import re
import csv


with open("phonebook_raw.csv", encoding='utf8') as f:
    rows = list(csv.reader(f, delimiter=","))
    headers = rows[0]
    contacts_list = sorted(rows[1:], key=lambda x: (x[0], x[1]))


clear_contact_list = []
phone_pattern = r'^(\+7|7|8)?[\s\-]*\(?([489][0-9]{2})\)?[\s\-]*(\d{3})[\s\-]*(\d{2})[\s\-]*(\d{2})'
additional_phone_pattern = r'\(?[а-яёА-ЯЁ]+[\s\.]*(\d+)\)?$'
for contact in contacts_list:
    fio = [x for x in ' '.join(contact[:2]).split(' ') if x]
    if len(fio) == 2:
        fio.append('')
    re_phone = re.findall(phone_pattern, contact[5])
    re_add_phone = re.findall(additional_phone_pattern, contact[5])
    phone = None
    if re_phone:
        phone = f'+7 ({re_phone[0][1]}) {re_phone[0][2]}-{re_phone[0][3]}-{re_phone[0][4]}'
        if re_add_phone:
            phone += f' добавочный {re_add_phone[0]}'
    clear_contact_list.append(
        (
            fio[0],
            fio[1],
            fio[2],
            contact[3],
            contact[4],
            phone,
            contact[6],
        )
    )

merged_contacts_list = []
prev = None
for enum, contact in enumerate(clear_contact_list):
    if prev:
        if contact[0] == prev[0] and contact[1] == prev[1]:
            merged_contacts_list.pop()
            merged_contacts_list.append([x or y for x, y in zip(prev, contact)])
            prev = contact
            continue
    merged_contacts_list.append(contact)
    prev = contact


with open("phonebook.csv", "w", encoding='utf-8') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerow(headers)
    datawriter.writerows(merged_contacts_list)
