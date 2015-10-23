class FizzBuzz
  def fizz? n
    n % 3 == 0 and n > 0
  end

  def buzz? n
    n % 5 == 0 and n > 0
  end

  def fizzbuzz n
    result = ''

    if fizz? n
      result += 'fizz'
    end
    if buzz? n
      result += 'buzz'
    end

    result == '' ? n : result
  end
end
