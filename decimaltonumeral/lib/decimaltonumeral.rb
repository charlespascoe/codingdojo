class DecimalToNumeral
  NUMS = {10 => 'X', 9 => 'IX', 5 => 'V', 4 => 'IV', 1 => 'I'}
  def self.convert i
    out = ''
    NUMS.each do |k, v| 
      while i >= k
        out << v
        i -= k
      end
    end
    return out
  end
end

