<script>
	let total = 0;
	let pts_this_round = 0
	let r1, r2, r3, r4, r5 = 0;
	let last_roll = 0;

	function roll(){
		let r = Math.ceil(Math.random() * 6)
		last_roll = r
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
					<h1 class="title">Board</h1>
					<h1 class="subtitle">Total score: {total}</h1>
					<h1 class="subtitle">Last roll: {last_roll}</h1>
					<button class="button is-primary" on:click={roll}>Roll</button>
				</div>
			</div>
			<div class="column">
				<div class="box">
					<h1 class="title">Current Round</h1>
				</div>
			</div>
		</div>
	</div>
</main>