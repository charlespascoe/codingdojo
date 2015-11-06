require 'numbers_to_words'

describe NumbersToWords do
  describe '#to_word' do
    it "should return zero for 0" do
      expect(subject.to_word 0).to eq 'zero'
    end
    it "should return one for 1" do
      expect(subject.to_word 1).to eq 'one'
    end
    it "should return two for 2" do
      expect(subject.to_word 2).to eq 'two'
    end
  end
end
