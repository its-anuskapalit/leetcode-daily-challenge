class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        unique_numbers = set()
        
        for ones_index, ones_digit in enumerate(digits):
            if ones_digit & 1:
                continue
                
            for tens_index, tens_digit in enumerate(digits):
                if ones_index == tens_index:
                    continue
                    
                for hundreds_index, hundreds_digit in enumerate(digits):
                    if hundreds_digit == 0 or hundreds_index in (ones_index, tens_index):
                        continue
                        
                    number = hundreds_digit * 100 + tens_digit * 10 + ones_digit
                    unique_numbers.add(number)
                    
        return len(unique_numbers)
