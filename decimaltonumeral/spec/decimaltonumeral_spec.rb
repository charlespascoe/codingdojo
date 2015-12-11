require 'spec_helper'

describe "DecimalToNumeral" do
  describe "#convert" do
    it 'should convert 1 to I' do
      expect(DecimalToNumeral.convert(1)).to eq "I" 
    end
    it 'should convert 2 to II' do
      expect(DecimalToNumeral.convert(2)).to eq "II" 
    end
    it 'should convert 3 to III' do
      expect(DecimalToNumeral.convert(3)).to eq "III" 
    end
    it 'should convert 4 to IV' do
      expect(DecimalToNumeral.convert(4)).to eq "IV" 
    end
    it 'should convert 5 to V' do
      expect(DecimalToNumeral.convert(5)).to eq "V" 
    end
    it 'should convert 6 to VI' do
      expect(DecimalToNumeral.convert(6)).to eq "VI" 
    end
    it 'should convert 7 to VII' do
      expect(DecimalToNumeral.convert(7)).to eq "VII" 
    end
    it 'should convert 8 to VIII' do
      expect(DecimalToNumeral.convert(8)).to eq "VIII" 
    end
    it 'should convert 9 to IX' do
      expect(DecimalToNumeral.convert(9)).to eq "IX" 
    end
     end
end
