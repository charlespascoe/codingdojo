class Yahtzee
  VALUES = {aces: 1, twos: 2, threes: 3, fours: 4, fives: 5, sixes: 6}

  def score (dice, category)
    if VALUES.has_key? category
      return dice.count(VALUES[category]) * VALUES[category]
    elsif category == :pair
      return sum_of_run(dice, 2).max || 0
    elsif category == :two_pairs
      return sum_of_run(dice, 2).length == 2 ? sum_of_run(dice, 2).inject(:+) : 0
    elsif category == :three_of_a_kind
      return sum_of_run(dice, 3).max || 0
    elsif category == :four_of_a_kind
      return sum_of_run(dice, 4).max || 0
    elsif category == :small_straight
      return dice.sort == [1,2,3,4,5] ? 15 : 0
    elsif category == :large_straight
      return dice.sort == [2,3,4,5,6] ? 20 : 0
    elsif category == :full_house
      return sum_of_run(dice, 2).length == 1 && sum_of_run(dice, 3).length == 1 ? dice.inject(:+) : 0
    end
  end

  def sum_of_run (dice, size)
      dice.group_by{ |x| x }.values.select{ |x| x.length == size }.map{ |x| x.inject(:+) }
  end
end
