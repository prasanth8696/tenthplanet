
const prompt = require('prompt-sync')({signint : true});

getWingman = (pilots) => {
		wingman = [];
		max = -Infinity;
		for(let i=pilots.length-1;i>=0;i--){
			if(pilots[i] > max){
				wingman.unshift(pilots[i]);
				max = pilots[i];
                        }
		}
		return wingman;

	}


const pilots = prompt('enter pilot heights separated with space ').split(' ').map(Number);

console.log(getWingman(pilots))

