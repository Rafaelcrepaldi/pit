class NumberMapper:
    def __init__(self):
        self.number_map = self._create_number_map()

    def _create_number_map(self):
        units = ["", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
        teens = ["dez", "onze", "doze", "treze", "catorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]
        tens = ["", "dez", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]
        hundreds = ["", "cem", "duzentos", "trezentos", "quatrocentos", "quinhentos", "seiscentos", "setecentos", "oitocentos", "novecentos"]
        number_map = {}

        for i in range(1, 10):
            number_map[units[i]] = i

        for i in range(10, 20):
            number_map[teens[i - 10]] = i

        for i in range(2, 10):
            for j in range(0, 10):
                if j == 0:
                    number_map[tens[i]] = i * 10
                else:
                    number_map[f"{tens[i]} e {units[j]}"] = i * 10 + j

        for i in range(1, 10):
            for j in range(0, 100):
                if j == 0:
                    number_map[hundreds[i]] = i * 100
                else:
                    if j < 10:
                        number_map[f"{hundreds[i]} e {units[j]}"] = i * 100 + j
                    elif j < 20:
                        number_map[f"{hundreds[i]} e {teens[j - 10]}"] = i * 100 + j
                    else:
                        tens_part = j // 10
                        units_part = j % 10
                        if units_part == 0:
                            number_map[f"{hundreds[i]} e {tens[tens_part]}"] = i * 100 + j
                        else:
                            number_map[f"{hundreds[i]} e {tens[tens_part]} e {units[units_part]}"] = i * 100 + j

        for i in range(1, 10):
            for j in range(0, 1000):
                if j == 0:
                    number_map[f"{units[i]} mil"] = i * 1000
                else:
                    if j < 10:
                        number_map[f"{units[i]} mil e {units[j]}"] = i * 1000 + j
                    elif j < 20:
                        number_map[f"{units[i]} mil e {teens[j - 10]}"] = i * 1000 + j
                    elif j < 100:
                        tens_part = j // 10
                        units_part = j % 10
                        if units_part == 0:
                            number_map[f"{units[i]} mil e {tens[tens_part]}"] = i * 1000 + j
                        else:
                            number_map[f"{units[i]} mil e {tens[tens_part]} e {units[units_part]}"] = i * 1000 + j
                    else:
                        hundreds_part = j // 100
                        remainder = j % 100
                        if remainder == 0:
                            number_map[f"{units[i]} mil e {hundreds[hundreds_part]}"] = i * 1000 + j
                        else:
                            if remainder < 10:
                                number_map[f"{units[i]} mil e {hundreds[hundreds_part]} e {units[remainder]}"] = i * 1000 + j
                            elif remainder < 20:
                                number_map[f"{units[i]} mil e {hundreds[hundreds_part]} e {teens[remainder - 10]}"] = i * 1000 + j
                            else:
                                tens_part = remainder // 10
                                units_part = remainder % 10
                                if units_part == 0:
                                    number_map[f"{units[i]} mil e {hundreds[hundreds_part]} e {tens[tens_part]}"] = i * 1000 + j
                                else:
                                    number_map[f"{units[i]} mil e {hundreds[hundreds_part]} e {tens[tens_part]} e {units[units_part]}"] = i * 1000 + j

        return number_map

    def map_number(self, text):
        return self.number_map.get(text, text)  # Retorna o texto original se não encontrar no mapa
