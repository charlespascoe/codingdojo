require 'fizzbuzz'

describe FizzBuzz do
  describe '#fizz' do
    results = {0 => false, 1 => false, 3 => true, 5 => false, 6 => true, 9 => true, 10 => false}

    results.each do |key, val|
      it "should return #{val} for #{key}" do
        f = FizzBuzz.new
        expect(f.fizz key).to eq(val)
      end
    end
  end

  describe '#buzz' do
    results = {0 => false, 1 => false, 3 => false, 5 => true, 6 => false, 9 => false, 10 => true}

    results.each do |key, val|
      it "should return #{val} for #{key}" do
        f = FizzBuzz.new
        expect(f.buzz key).to eq(val)
      end
    end
  end

  describe '#fizzbuzz' do
    results = {0 => 0, 1 => 1, 3 => 'fizz', 5 => 'buzz', 6 => 'fizz', 9 => 'fizz', 10 => 'buzz', 15 => 'fizzbuzz', 30 => 'fizzbuzz', 50 => 'buzz'}

    results.each do |key, val|
      it "should return #{val} for #{key}" do
        f = FizzBuzz.new
        expect(f.fizzbuzz key).to eq(val)
      end
    end
  end
end

