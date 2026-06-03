import DroneCard from "./DroneCard";

export default function DroneGrid() {

  const drones = [
    { id: "D-01", battery: 82, survivors: 3 },
    { id: "D-02", battery: 67, survivors: 1 },
    { id: "D-03", battery: 91, survivors: 4 },
  ];

  return (
    <div className="grid grid-cols-2 gap-4">
      {drones.map((d) => (
        <DroneCard key={d.id} drone={d} />
      ))}
    </div>
  );
}