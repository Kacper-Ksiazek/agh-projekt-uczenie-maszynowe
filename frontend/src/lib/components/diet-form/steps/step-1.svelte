<script lang="ts">
import { dietState } from "../state.svelte";

import type {
  Gender,
  ActivityLevel,
  Goal,
  CookingTimePerDay,
} from "$lib/types";

import { Label } from "$lib/components/ui/label";
import { Input } from "$lib/components/ui/input";
import * as Select from "$lib/components/ui/select";
</script>

<div>
  <Label for="age">Wiek</Label>
  <Input id="age" type="number" bind:value={dietState.age} placeholder="Wiek" />
</div>

<div>
  <Label>Płeć</Label>
  <Select.Root>
    <Select.Trigger>
      <Select.Value placeholder="Wybierz płeć" />
    </Select.Trigger>

    <Select.Content>
      <Select.Item value={"MALE" as Gender}>Mężczyzna</Select.Item>
      <Select.Item value={"FEMALE" as Gender}>Kobieta</Select.Item>
    </Select.Content>
  </Select.Root>
</div>

<div>
  <Label for="weight">Waga [kg]</Label>
  <Input
    id="weight"
    type="number"
    min="0"
    bind:value={dietState.weight}
    placeholder="Waga"
  />
</div>

<div>
  <Label for="height">Wzrost [cm]</Label>
  <Input
    id="height"
    type="number"
    min="0"
    bind:value={dietState.height}
    placeholder="Wzrost"
  />
</div>

<div>
  <Label>Poziom aktywności fizycznej</Label>
  <Select.Root>
    <Select.Trigger>
      <Select.Value placeholder="Wybierz poziom aktywności" />
    </Select.Trigger>

    <Select.Content>
      <Select.Item value={"SEDENTARY" as ActivityLevel}>
        Siedzący tryb życia ( brak aktywności fizycznej )
      </Select.Item>
      <Select.Item value={"LIGHT" as ActivityLevel}>
        Lekka aktywność fizyczna ( 1-3 dni w tygodniu )
      </Select.Item>
      <Select.Item value={"MODERATE" as ActivityLevel}>
        Umiarkowana aktywność fizyczna ( 3-5 dni w tygodniu )
      </Select.Item>
      <Select.Item value={"ACTIVE" as ActivityLevel}>
        Wysoka aktywność fizyczna ( 5-7 dni w tygodniu )
      </Select.Item>
    </Select.Content>
  </Select.Root>
</div>

<div>
  <Label>Cel diety</Label>
  <Select.Root>
    <Select.Trigger>
      <Select.Value placeholder="Wybierz cel diety" />
    </Select.Trigger>

    <Select.Content>
      <Select.Item value={"WEIGHT_LOSS" as Goal}>Redukcja</Select.Item>
      <Select.Item value={"WEIGHT_MAINTENANCE" as Goal}
        >Utrzymanie wagi</Select.Item
      >
      <Select.Item value={"WEIGHT_GAIN" as Goal}>Przybranie wagi</Select.Item>
    </Select.Content>
  </Select.Root>
</div>

<div>
  <Label>Ile średnio dziennie masz czasu na przygotowanie posiłków?</Label>
  <Select.Root>
    <Select.Trigger>
      <Select.Value placeholder="Wybierz czas" />
    </Select.Trigger>

    <Select.Content>
      <Select.Item value={"30_MINUTES" as CookingTimePerDay}
        >Mniej niż 30 minut</Select.Item
      >
      <Select.Item value={"1_HOUR" as CookingTimePerDay}>
        30 minut - 1 godzina
      </Select.Item>

      <Select.Item value={"OVER_1_HOUR" as CookingTimePerDay}>
        Powyżej godziny
      </Select.Item>
    </Select.Content>
  </Select.Root>
</div>
