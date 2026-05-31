export default function ControlPanel() {
  return (
    <div className="bg-gray-900 p-4 rounded-xl mt-4">

      <h2 className="text-yellow-400 text-xl font-bold">
        CONTROL PANEL
      </h2>

      <div className="flex flex-col gap-3 mt-4">

        <button className="bg-cyan-600 p-2 rounded">
          Deploy Drone Swarm
        </button>

        <button className="bg-red-600 p-2 rounded">
          Start Thermal Scan
        </button>

        <button className="bg-green-600 p-2 rounded">
          Analyze Survivors
        </button>

      </div>

    </div>
  );
}