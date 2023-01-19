<script>
    export let cur_condition;
</script>


<main>
   <div class="p-3 w-full bg-neutral-500 flex">
        <div class="w-2/3 bg-inherit text-3xl p-3">
            {#if cur_condition != undefined}
                {#if cur_condition.l_precip_rate > 1.0}
                    You may want to bring an umbrella with you...
                {:else if cur_condition.l_precip_rate > 0}
                    It is raining lightly...
                {/if}
            {/if}
        </div>
        <div class="w-1/3 p-3 bg-white rounded-lg text-right">
            <div class="text-5xl pb-3 font-bold">
                {#if cur_condition != undefined}
                    {cur_condition.air_temp} °C
                {/if}
            </div>
            <div>
                {#if cur_condition != undefined}
                    {cur_condition.l_precip_rate} mm/hr
                {/if} 
            </div>
            <div>
                {#if cur_condition != undefined}
                    {cur_condition.pressure} Pa
                {/if} 
            </div>
            <div>
                {#if cur_condition != undefined}
                    {cur_condition.wind_speed} km/h
                {/if} 
            </div>
        </div>
   </div>
</main>

<style>
</style>