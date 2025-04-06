<script lang="ts">
import { dietState } from "../state.svelte";

import { Label } from "$lib/components/ui/label";
import { Input } from "$lib/components/ui/input";
</script>

<div class="flex flex-col gap-1">
  <Label for="numberOfDays">Ilość dni</Label>
  <Input
    id="numberOfDays"
    type="number"
    bind:value={dietState.numberOfDays}
    min={1}
    max={5}
    placeholder="Ilość dni (1-5) na które chcesz wygenerować jadłospis"
  />
</div>

<div class="flex flex-col gap-1">
  <Label for="numberOfDays">Budżet [zł]</Label>
  <Input
    id="numberOfDays"
    type="number"
    bind:value={dietState.budget}
    min={0}
    placeholder="Budżet [zł] na cały okres diety"
  />
</div>
