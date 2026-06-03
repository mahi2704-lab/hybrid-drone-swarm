export default function DroneCard({ drone }) {
  return (
    <div className="bg-gray-900 p-4 rounded-xl border border-cyan-500">

      <h2 className="text-cyan-400 text-xl font-bold">
        {drone.id}
      </h2>

      <div className="mt-3">
        <p>Battery: {drone.battery}%</p>
        <p>Status: ACTIVE</p>
        <p>Survivors Found: {drone.survivors}</p>
      </div>

    </div>
  );
}