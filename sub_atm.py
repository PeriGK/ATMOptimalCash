from atm_machine import ATMMachine


class SubATMTest(ATMMachine):
    def is_amount_fully_withdrawable(self, amount):
        return super()._is_amount_fully_withdrawable(amount)

    def set_sum_notes(self, minimum_number_notes_dict):
        return super()._set_notes_dict(minimum_number_notes_dict)

    def split_amount_to_notes(self, amount):
        return super()._split_amount_to_notes(amount)
