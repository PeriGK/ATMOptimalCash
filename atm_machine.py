class ATMMachine:

    def __init__(self, notes_dict={20: 100, 50: 75}, sum_notes=5750, currency='$'):
        self.notes_dict = notes_dict
        self.sum_notes = sum_notes
        self.currency = currency

    def withdraw(self, amount):
        is_amount_fully_withdrawable = self._is_amount_fully_withdrawable(amount)
        is_amount_sufficient = self._get_sum_notes() > amount
        if is_amount_sufficient and is_amount_fully_withdrawable:
            minimum_number_notes_dict = self._split_amount_to_notes(amount)
            self._set_notes_dict(minimum_number_notes_dict)
            self._set_sum_notes(amount)
            print('Withdrawal was successful')
            return minimum_number_notes_dict
        else:
            if not is_amount_sufficient:
                print('It is not possible to withdraw the given amount. Available amount is less than the '
                      'requested one {}{}'.format(amount, self.currency))
            if not is_amount_fully_withdrawable:
                print('It is not possible to fully withdraw {}{}. The amount should be a multiplier of {}'
                      .format(amount, self.currency, list(self.notes_dict.keys())))
            return {}

    def _set_notes_dict(self, minimum_number_notes_dict):
        print(minimum_number_notes_dict)
        for k, v in minimum_number_notes_dict.items():
            self.notes_dict[k] -= v

    def _get_sum_notes(self):
        return self.sum_notes

    def _set_sum_notes(self, amount):
        self.sum_notes -= amount

    def _is_amount_fully_withdrawable(self, amount):
        notes_descending_order = sorted(list(self.notes_dict.keys()), reverse=True)
        for note in notes_descending_order:
            while amount >= note:
                amount -= note
        return amount == 0

    def _split_amount_to_notes(self, amount):
        notes_descending_order = sorted(list(self.notes_dict.keys()), reverse=True)
        minimum_number_notes_dict = {}.fromkeys(notes_descending_order, 0)
        for note in notes_descending_order:
            while amount >= note:
                minimum_number_notes_dict[note] += 1
                amount -= note

        return minimum_number_notes_dict

    def __str__(self):
        output = ["Current amount in the ATM:"]
        for key, value in self.notes_dict.items():
            output.append("{} pieces of {}{} notes".format(value, self.currency, key))

        output.append("A total of: {}{}".format(self.currency, self._get_sum_notes()))

        return "\n".join(output)

