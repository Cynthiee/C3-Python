


// using function 

function isPrime(num) {

    if (num < 2) {
        return "is not a prime number"
    }

    if (num === 2) {
        return "is a prime number"
    }

    for (let i = 3; i < num; i++) {
        if (num % i === 0) {
        return "is not a prime number"    
        }        
    }
    return "is a prime number"
}

console.log(isPrime(10));





