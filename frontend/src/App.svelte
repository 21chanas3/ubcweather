<script>
	import { onMount } from "svelte";
	import CurrentConditions from './components/CurrentConditions.svelte'
    import TemperatureChart from "./components/TemperatureChart.svelte";

	let cur_condition;
	let past_conditions;

	async function getCurrentConditions() {
		let resp = await fetch("/api/current").then((res) => res.json());
		cur_condition = JSON.stringify(resp);
		cur_condition = JSON.parse(cur_condition);
	}

	async function getPastConditions() {
		let resp = await fetch("/api/current").then((res) => res.json());
		cur_condition = JSON.stringify(resp);
		cur_condition = JSON.parse(cur_condition);
	}
    
    onMount(getCurrentConditions);
	onMount(getPastConditions);
</script>

<main>
	<CurrentConditions {cur_condition}/>
	<TemperatureChart {past_conditions}/>
</main>

<svelte:head>
	<script src="https://cdn.tailwindcss.com"></script>
	<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.3.0/font/bootstrap-icons.css">
</svelte:head>

<style>
</style>