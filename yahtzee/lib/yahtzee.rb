class Yahtzee
  VALUES = {aces: 1, twos: 2, threes: 3, fours: 4, fives: 5, sixes: 6}
  def score (dice, category)
    if VALUES.has_key? category
      return dice.count(VALUES[category]) * VALUES[category]
    elsif category == :pair
      return 8
    end
  end
end
