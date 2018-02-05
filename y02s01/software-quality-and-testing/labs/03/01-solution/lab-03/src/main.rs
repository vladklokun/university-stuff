use std::cmp::Ordering;

fn count_signs(v: &Vec<i32>) -> Vec<i32> {
	let mut negative_count = 0;
	let mut neutral_count = 0;
	let mut positive_count = 0;
	
	for el in v.iter() {
		match el.cmp(&0) {
			Ordering::Less	=> negative_count += 1,
			Ordering::Greater	=> positive_count += 1,
			Ordering::Equal	=> neutral_count += 1,
		}
	}
	
	let res = vec![negative_count, neutral_count, positive_count];
	
	res
}

fn find_most_freq_sign(v: &Vec<i32>) -> char {
	//Since function takes a vector of frequency of numbers with signs
	//in a fixed format (neg, neutral, pos), we match indices
	//to respective values.
	
	let sign_count = count_signs(v);
	
	if sign_count == [0,0,0] {
		//If all frequencies equal zero, return '0' as the most frequent sign.
		return '0'
	}

	println!("tmp: {:?}", sign_count);
	
	match sign_count.iter().position(|&el| &el == sign_count.iter().max().unwrap()) {
		Some(0) => '-',
		Some(2) => '+',
		_ => '0',
	}
}

fn main() {
	let a = vec![];
	
	println!("Result: {:?}", find_most_freq_sign(&a));
}

#[cfg(test)]
mod tests {
	use super::*;
	
	#[test]
	fn case1() {
		let a = vec![];
		
		assert_eq!('0', find_most_freq_sign(&a));
	}
	
	#[test]
	fn case2() {
		let a = vec![1,2,3,4,5];
		assert_eq!('+', find_most_freq_sign(&a));
	}
	
	#[test]
	fn case3() {
		let a = vec![-5,-4,-3,-2,-1];
		assert_eq!('-', find_most_freq_sign(&a));
	}
	
	#[test]
	#[should_panic]
	fn case4() {
		let a = vec![-1,1,-2,2,-3,3];
		assert_ne!('-', find_most_freq_sign(&a));
	}
}