<script lang="ts">
import {
  activityLevelOptions,
  cookingTimeOptions,
  genderOptions,
  goalOptions,
} from "../options";
import { dietState } from "../state.svelte";

function displayOptional(value: string) {
  return value.length ? value : "-";
}
</script>

<div class="text-sm">
  <!-- Step 1 -->
  <div class="mb-6">
    <h3 class="mb-2 text-xl font-semibold">Krok 1.</h3>
    <ul class="list-inside list-disc">
      <li>
        <span>Płeć:</span>
        <strong>
          {genderOptions.find(
        (option) => option.value === dietState.gender,
        )?.label ?? "N/A"}
        </strong>
      </li>
      <li><span>Wiek:</span> <strong>{dietState.age}</strong></li>
      <li><span>Wzrost:</span> <strong>{dietState.height} cm</strong></li>
      <li><span>Waga:</span> <strong>{dietState.weight} kg</strong></li>
      <li>
        <span>Cel diety:</span>
        <strong>
          {goalOptions.find(
        (option) => option.value === dietState.goal,
        )?.label ?? "N/A"}
        </strong>
      </li>
      <li>
        <span>Poziom aktywności fizycznej:</span>
        <strong>
          {activityLevelOptions.find(
            (option) => option.value === dietState.activityLevel,
        )?.label ?? "N/A"}
        </strong>
      </li>
      <li>
        <span>Czas na gotowanie:</span>
        <strong>
          {cookingTimeOptions.find(
            (option) => option.value === dietState.cookingTime,
        )?.label ?? "N/A"}
        </strong>
      </li>
    </ul>
  </div>

  <hr class="my-4 border-t border-gray-300" />

  <!-- Step 2 -->
  <div class="mb-6">
    <h3 class="mb-2 text-xl font-semibold">Krok 2.</h3>
    <ul class="list-inside list-disc">
      <li>
        <span>Alergie:</span>
        <strong>
          {displayOptional(dietState.allergies)}
        </strong>
      </li>
      <li>
        <span>Nietolerancje:</span>
        <strong>
          {displayOptional(dietState.intolerance)}
        </strong>
      </li>
      <li>
        <span>Nielubiane produkty: </span>
        <strong>
          {displayOptional(dietState.dislikedFoods)}
        </strong>
      </li>
      <li>
        <span>Preferencje kulinarne:</span>
        <strong>
          {displayOptional(dietState.preferredFoods)}
        </strong>
      </li>
      <li>
        <span>Sprzęt kuchenny:</span>
        <strong>
          {displayOptional(dietState.kitchenEquipment)}
        </strong>
      </li>
    </ul>
  </div>

  <hr class="my-4 border-t border-gray-300" />

  <!-- Step 3 -->
  <div>
    <h3 class="mb-2 text-xl font-semibold">Krok 3.</h3>
    <ul class="list-inside list-disc">
      <li><span>Ilość dni:</span> <strong>{dietState.numberOfDays}</strong></li>
      <li>
        <span>Budżet na całą dietę:</span>
        <strong>{dietState.budget} zł</strong>
      </li>
    </ul>
  </div>
</div>
