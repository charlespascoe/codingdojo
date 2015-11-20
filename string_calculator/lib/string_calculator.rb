class Calculator
  def add s
    delimiter_regex = /\/\/(.+)?\\n/
    delimiter = s[delimiter_regex, 1] || /,|\\n/
    return s == '' ? 0 : s.sub(delimiter_regex, '').split(delimiter).map(&:to_f).reduce(:+)
  end
end
