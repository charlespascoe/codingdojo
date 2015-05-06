coins :: [Integer]
coins = [200,100,50,20,10,5,2,1]

change :: Integer -> [Integer]
change 0 = []
change n = x : change (n - x)
	where x = head (filter (<=n) coins)

