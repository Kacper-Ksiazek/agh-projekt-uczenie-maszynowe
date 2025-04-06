<script lang="ts">
import type { AIGeneratedDietPlan, AIGeneratedSingleMeal } from "$lib/types";

const { data } = $props<{ data: AIGeneratedDietPlan }>();
</script>

{#snippet renderMeal(meal:AIGeneratedSingleMeal, index: number)}
  <div class="rounded-xl bg-white p-6 shadow-md transition hover:shadow-lg">
    <h3 class="mb-2 text-xl font-semibold text-slate-800">
      Danie {index + 1}. - {meal.name}
    </h3>
    <p class="mb-4 text-slate-600">{meal.description}</p>

    <div class="mb-4">
      <p class="font-medium text-slate-700">Składniki:</p>
      <ul class="list-inside list-disc text-slate-600">
        {#each meal.ingredients as ingredient}
          <li>{ingredient}</li>
        {/each}
      </ul>
    </div>

    <div class="mb-4">
      <p class="font-medium text-slate-700">Przygotowanie:</p>
      <ol class="list-inside list-decimal text-slate-600">
        {#each meal.recipe_in_steps as step}
          <li>{step}</li>
        {/each}
      </ol>
    </div>

    <div>
      <p class="font-medium text-slate-700">Wartości odżywcze:</p>
      <ul class="text-slate-600">
        <li>
          <span class="font-semibold">Białko:</span>
          {meal.macros.protein} g
        </li>
        <li>
          <span class="font-semibold">Tłuszcze:</span>
          {meal.macros.fat} g
        </li>
        <li>
          <span class="font-semibold">Węglowodany:</span>
          {meal.macros.carbs} g
        </li>
        <li>
          <span class="font-semibold">Kalorie:</span>
          {meal.macros.calories} kcal
        </li>
      </ul>
    </div>
  </div>
{/snippet}

{#snippet renderDay(day:AIGeneratedSingleMeal[], index: number)}
  <div
    class="w-full rounded-2xl border border-slate-300 bg-slate-50 p-6 shadow-inner"
  >
    <h2 class="mb-4 text-2xl font-bold text-slate-700">Dzień {index + 1}</h2>

    <div class="grid gap-6 md:grid-cols-1">
      {#each day as meal, index}
        {@render renderMeal(meal, index)}
      {/each}
    </div>
  </div>
{/snippet}

<section class="mx-auto flex w-full max-w-5xl flex-col gap-8 p-10">
  {#each data as day, index}
    {@render renderDay(day, index)}
  {/each}
</section>
