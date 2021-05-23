import re

fhandle = open('gotham_op.txt')
invalid_input = 0
count = dict()
wrong_input = dict()
key = 0
for line in fhandle:  # percorre todas as linhas do arquivo
    line = line.strip()
    if line.startswith("SIDE:"):  # verifica se a linha está correta
        pos = line.find(":")
        sale_pos = line.find(";", pos)
        fst_value = line[pos+1:sale_pos]
        if fst_value == "BUY":
            lst = re.findall('QTY:([^ ]+?);', line)
            value = int(lst[0])
            if value > 0 and value % 10 == 0:
                if re.findall('[A-Z]{4}[0-9]{1}', line):  # verifica se possui 4 letras e 1 digito
                    lst_ativo = re.findall('[A-Z]{4}[0-9]{1}', line)
                    ativo = lst_ativo[0]
                    count[ativo] = count.get(ativo, 0) + value
                elif re.findall('[A-Z]{4}[0-9]{2}', line):  # verifica se possui 4 letras e 2 digitos
                    lst_ativo = re.findall('[A-Z]{4}[0-9]{2}', line)
                    ativo = lst_ativo[0]
                    count[ativo] = count.get(ativo, 0) + value
        elif fst_value == "SELL":
            lst = re.findall('QTY:([^ ]+?);', line)
            value = int(lst[0])
            if value > 0 and value % 10 == 0:
                if re.findall('[A-Z]{4}[0-9]{1}', line):  # verifica se possui 4 letras e 1 digito
                    lst_ativo = re.findall('[A-Z]{4}[0-9]{1}', line)
                    ativo = lst_ativo[0]
                    count[ativo] = count.get(ativo, 0) - value
                elif re.findall('[A-Z]{4}[0-9]{2}', line):  # verifica se possui 4 letras e 2 digitos
                    lst_ativo = re.findall('[A-Z]{4}[0-9]{2}', line)
                    ativo = lst_ativo[0]
                    count[ativo] = count.get(ativo, 0) - value
        if fst_value != "BUY" and fst_value != "SELL":  # avalia entradas erradas
            wrong_input[key] = wrong_input.get(key, "") + "Valor inválido de SIDE; "
            lst = re.findall('QTY:([^ ]+?);', line)
            value = int(lst[0])
        if value > 0 and value % 10 == 0:
            if re.findall('TICKER:([A-Z]{4}[0-9]{1})', line) or re.findall('TICKER:([A-Z]{4}[0-9]{2})', line):
                pass
            else:
                wrong_input[key] = wrong_input.get(key, "") + "TICKER mal formatado."
        elif value < 0:
            wrong_input[key] = wrong_input.get(key, "") + "QTY não é positivo; "
            if re.findall('TICKER:([A-Z]{4}[0-9]{1})', line) or re.findall('TICKER:([A-Z]{4}[0-9]{2})', line):
                pass
            else:
                wrong_input[key] = wrong_input.get(key, 0) + "TICKER mal formatado."
        elif value % 10 != 0:
            wrong_input[key] = wrong_input.get(key, "") + "QTY não é múltiplo de 10; "
            if re.findall('TICKER:([A-Z]{4}[0-9]{1})', line) or re.findall('TICKER:([A-Z]{4}[0-9]{2})', line):
                pass
            else:
                wrong_input[key] = wrong_input.get(key, "") + "TICKER mal formatado."
        else:
            if re.findall('TICKER:([A-Z]{4}[0-9]{1})', line) or re.findall('TICKER:([A-Z]{4}[0-9]{2})', line):
                pass
            else:
                wrong_input[key] = wrong_input.get(key, "") + "TICKER mal formatado."
        key += 1



# imprimindo os resultados
for k in count:
    print("{}: {}".format(k, count[k]))

for k in wrong_input:
    print("{}".format(wrong_input[k]))
