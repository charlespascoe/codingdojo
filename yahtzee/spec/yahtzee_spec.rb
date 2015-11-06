require 'yahtzee'

describe Yahtzee do
  describe '#score' do
    describe 'single categories' do
      tests = [
        {dice: [1,1,2,3,4], category: :aces,  score: 2 },
        {dice: [1,3,4,3,6], category: :twos,  score: 0 },
        {dice: [2,4,4,2,1], category: :fours, score: 8 },
        {dice: [6,6,6,6,6], category: :sixes, score: 30}
      ]

      tests.each do |test|
        it "should return #{test[:score]} for #{test[:dice]} in category #{test[:category]}" do
          expect(subject.score(test[:dice], test[:category])).to eq test[:score]
        end
      end
    end

    describe 'pair category' do
      tests = [
        {dice: [3,3,3,4,4], score: 8}
      ]

      tests.each do |test|
        it "should return #{test[:score]} for #{test[:dice]} in category pair" do
          expect(subject.score(test[:dice], :pair)).to eq test[:score]
        end
      end
    end
  end
end
