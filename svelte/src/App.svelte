<script>
	let total = 0;
	let pts_this_round = 0
	let r1, r2, r3, r4, r5 = 0;
	let last_roll = 0;
	let round = 1
	var game_ended = false;
	function end_game(){
		game_ended = true
	}

	function next_round(){
		if (round == 5){
			return end_game()
		}
		total += pts_this_round
		last_roll = 0
		pts_this_round = 0
		round += 1
	}

	function roll(){
		let r = Math.ceil(Math.random() * 6)
		if (r == 6){ 
			pts_this_round = 0
			alert("You rolled a 6!")
			return next_round()
		}
		last_roll = r
		pts_this_round += r
	}
</script>
<br><br>
<main>
	<div class="container">
		<div class="columns">
			<div class="column">
				<div class="box">
					<h1 class="title">Round scores</h1>
				</div>
			</div>
			<div class="column">
				<div class="box">
					<h1 class="title">Round #{round}</h1>
					<h1 class="subtitle">Total score: {total}</h1>
					<h1 class="subtitle">Possible points: {pts_this_round}</h1>
					<h1 class="subtitle">Last roll: {last_roll}</h1>
					<div class="is-flex is-justify-content-center is-flex-direction-row">
						<button class="button is-primary mx-3 "  disabled={game_ended} on:click={roll}>Roll</button>
						<button class="button is-info mx-3 " disabled={game_ended} on:click={next_round}>End round</button>
					</div>
				</div>
			</div>
			<div class="column">
				<div class="box">
					<h1 class="title">Current Round</h1>
				</div>
			</div>
		</div>
		{#if game_ended}
			<div class="has-text-centered">
				<h1 class="title">Woohoo!</h1>
				<h3 class="subtitle">Your final score was {total}</h3>
			</div>
		{/if}
	</div>
</main>