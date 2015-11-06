class NumbersToWords
  LT20 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
  TENS = {20 => 'twenty', 30 => 'thirty', 40 => 'fourty', 50 => 'fifty', 60 => 'sixty', 70 => 'seventy', 80 => 'eighty', 90 => 'ninety'}
  NUMBERS = {100 => 'hundred', 1000 => 'thousand'}
  def to_word n
    return 'zero' if n == 0
    return 'one' if n == 1
    return 'two' if n == 2
  end
end
