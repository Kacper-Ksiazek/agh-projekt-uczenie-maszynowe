<script lang="ts">
import { dietState } from "../state.svelte";

import type {
  ActivityLevel,
  Goal,
  CookingTimePerDay,
  Gender,
} from "$lib/types";

import { Label } from "$lib/components/ui/label";
import { Input } from "$lib/components/ui/input";
import * as Select from "$lib/components/ui/select";
import {
  activityLevelOptions,
  cookingTimeOptions,
  genderOptions,
  goalOptions,
} from "../options";

let selectedGender = $derived(
  genderOptions.find(({ value }) => value === dietState.gender),
);

let selectedActivityLevel = $derived(
  activityLevelOptions.find(({ value }) => value === dietState.activityLevel),
);

let selectedGoal = $derived(
  goalOptions.find(({ value }) => value === dietState.goal),
);

let selectedCookingTime = $derived(
  cookingTimeOptions.find(({ value }) => value === dietState.cookingTime),
);
</script>

<div class="flex flex-col gap-1">
  <Label>Płeć</Label>
  <Select.Root
    selected={selectedGender}
    onSelectedChange={(selected)=>{
    dietState.gender = selected!.value as Gender
  }}
  >
    <Select.Trigger>
      <Select.Value placeholder="Wybierz płeć" />
    </Select.Trigger>

    <Select.Content>
      {#each genderOptions as option}
        <Select.Item value={option.value} label={option.label} />
      {/each}
    </Select.Content>
  </Select.Root>
</div>

<div class="flex flex-col gap-1">
  <Label for="age">Wiek</Label>
  <Input id="age" type="number" bind:value={dietState.age} placeholder="Wiek" />
</div>

<div class="flex flex-col gap-1">
  <Label for="weight">Waga [kg]</Label>
  <Input
    id="weight"
    type="number"
    min="0"
    bind:value={dietState.weight}
    placeholder="Waga"
  />
</div>

<div class="flex flex-col gap-1">
  <Label for="height">Wzrost [cm]</Label>
  <Input
    id="height"
    type="number"
    min="0"
    bind:value={dietState.height}
    placeholder="Wzrost"
  />
</div>

<div class="flex flex-col gap-1">
  <Label for="activityLevel">Poziom aktywności fizycznej</Label>
  <Select.Root
    name="activityLevel"
    selected={selectedActivityLevel}
    onSelectedChange={(selected) => {
      dietState.activityLevel = selected!.value as ActivityLevel;
    }}
  >
    <Select.Trigger>
      <Select.Value placeholder="Wybierz poziom aktywności" />
    </Select.Trigger>

    <Select.Content>
      {#each activityLevelOptions as option}
        <Select.Item value={option.value} label={option.label} />
      {/each}
    </Select.Content>
  </Select.Root>
</div>

<div class="flex flex-col gap-1">
  <Label>Cel diety</Label>
  <Select.Root
    selected={selectedGoal}
    onSelectedChange={(selected) => {
    dietState.goal = selected!.value as Goal;
  }}
  >
    <Select.Trigger>
      <Select.Value placeholder="Wybierz cel diety" />
    </Select.Trigger>

    <Select.Content>
      {#each goalOptions as option}
        <Select.Item value={option.value} label={option.label} />
      {/each}
    </Select.Content>
  </Select.Root>
</div>

<div class="flex flex-col gap-1">
  <Label>Ile średnio dziennie masz czasu na przygotowanie posiłków?</Label>
  <Select.Root
    selected={selectedCookingTime}
    onSelectedChange={(selected) => {
      dietState.cookingTime = selected!.value as CookingTimePerDay;
    }}
  >
    <Select.Trigger>
      <Select.Value placeholder="Wybierz czas" />
    </Select.Trigger>

    <Select.Content>
      {#each cookingTimeOptions as option}
        <Select.Item value={option.value} label={option.label} />
      {/each}
    </Select.Content>
  </Select.Root>
</div>
