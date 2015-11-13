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
        {dice: [3,3,3,4,4], score: 8 },
        {dice: [2,2,3,5,5], score: 10},
        {dice: [2,1,3,6,5], score: 0 },
        {dice: [2,2,2,6,5], score: 0 }
      ]

      tests.each do |test|
        it "should return #{test[:score]} for #{test[:dice]} in category pair" do
          expect(subject.score(test[:dice], :pair)).to eq test[:score]
        end
      end
    end

    describe 'two_pairs category' do
      tests = [
        {dice: [3,3,3,4,4], score: 0 },
        {dice: [2,2,3,5,5], score: 14},
        {dice: [2,1,3,6,5], score: 0 },
        {dice: [2,2,2,6,5], score: 0 }
      ]

      tests.each do |test|
        it "should return #{test[:score]} for #{test[:dice]} in category two_pairs" do
          expect(subject.score(test[:dice], :two_pairs)).to eq test[:score]
        end
      end
    end

    describe 'three_of_a_kind category' do
      tests = [
        {dice: [1,1,1,2,3], score: 3},
        {dice: [1,1,1,1,3], score: 0},
        {dice: [1,1,3,2,3], score: 0}
      ]

      tests.each do |test|
        it "should return #{test[:score]} for #{test[:dice]} in category three_of_a_kind" do
          expect(subject.score(test[:dice], :three_of_a_kind)).to eq test[:score]
        end
      end
    end

    describe 'four_of_a_kind category' do
      tests = [
        {dice: [1,1,1,1,3], score: 4},
        {dice: [2,2,2,2,3], score: 8},
        {dice: [1,1,1,2,3], score: 0},
        {dice: [5,5,5,5,5], score: 0}
      ]

      tests.each do |test|
        it "should return #{test[:score]} for #{test[:dice]} in category four_of_a_kind" do
          expect(subject.score(test[:dice], :four_of_a_kind)).to eq test[:score]
        end
      end
    end

    describe 'small_straight category' do
      tests = [
        {dice: [1,2,3,4,5], score: 15},
        {dice: [5,3,1,2,4], score: 15},
        {dice: [1,2,3,4,3], score: 0 },
        {dice: [5,5,5,5,5], score: 0 }
      ]

      tests.each do |test|
        it "should return #{test[:score]} for #{test[:dice]} in category small_straight" do
          expect(subject.score(test[:dice], :small_straight)).to eq test[:score]
        end
      end
    end

    describe 'large_straight category' do
      tests = [
        {dice: [2,3,4,5,6], score: 20},
        {dice: [5,3,6,2,4], score: 20},
        {dice: [5,2,3,4,3], score: 0 },
        {dice: [6,6,6,6,6], score: 0 }
      ]

      tests.each do |test|
        it "should return #{test[:score]} for #{test[:dice]} in category large_straight" do
          expect(subject.score(test[:dice], :large_straight)).to eq test[:score]
        end
      end
    end

    describe 'full_house category' do
      tests = [
        {dice: [2,2,4,4,4], score: 16},
        {dice: [5,3,3,3,4], score: 0 },
        {dice: [5,5,3,5,3], score: 21},
        {dice: [6,6,6,6,6], score: 0 }
      ]

      tests.each do |test|
        it "should return #{test[:score]} for #{test[:dice]} in category full_house" do
          expect(subject.score(test[:dice], :full_house)).to eq test[:score]
        end
      end
    end
  end
end
