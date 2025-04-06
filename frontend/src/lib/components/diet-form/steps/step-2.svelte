<script lang="ts">
import { dietState } from "../state.svelte";

import { Label } from "$lib/components/ui/label";
import { Input } from "$lib/components/ui/input";
import Textarea from "$lib/components/ui/textarea/textarea.svelte";
</script>

<div>
  <Label for="allergies">Alergie</Label>
  <Input
    id="allergies"
    bind:value={dietState.allergies}
    placeholder="Opisz swoje alergie (opcjonalne)"
  />
</div>

<div>
  <Label for="intolerances">Nietolerancje</Label>
  <Input
    id="intolerances"
    bind:value={dietState.intolerance}
    placeholder="Opisz swoje nietolerancje (opcjonalne)"
  />
</div>

<div>
  <Label for="dislikes">Nielubiane produkty</Label>
  <Textarea
    id="dislikes"
    bind:value={dietState.dislikedFoods}
    placeholder="Opisz swoje nielubiane produkty (opcjonalne)"
  />
</div>

<div>
  <Label for="dislikes">Preferencje kulinarne</Label>
  <Textarea
    id="dislikes"
    bind:value={dietState.dislikedFoods}
    placeholder="Opisz swoje preferencje kulinarne (opcjonalne)"
  />
</div>

<div>
  <Label for="kitchenEquipment">Doprecyzuj co posiadasz w kuchni</Label>
  <Textarea
    id="kitchenEquipment"
    bind:value={dietState.kitchenEquipment}
    placeholder="Doprecyzuj co posiadasz w kuchni (opcjonalne)"
  />
</div>
