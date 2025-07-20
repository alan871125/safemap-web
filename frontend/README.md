# SafeMap Frontend

This frontend is part of the SafeMap project, providing a web interface for safe route planning.

## Original Source

This implementation is based on the Google Maps Directions tutorial by [Truly Mittal](https://github.com/trulymittal/google-maps-directions-tutorial). The original tutorial covers:

1. Google maps in React
2. Adding Markers
3. Panning and zooming maps
4. Disable default controls
5. Places Autocomplete
6. Directions Service
7. Directions Renderer on map

**Original Youtube tutorial:** [https://youtu.be/iP3DnhCUIsE](https://youtu.be/iP3DnhCUIsE)

## SafeMap Extensions

We've extended the original code to include:
- Integration with SafeMap backend API
- Safety score visualization
- Custom route optimization based on safety metrics
- Enhanced user interface for safety-focused routing

## Starting the app

Create an API in the google developers console [https://console.developers.google.com](https://console.developers.google.com), make sure to enable billing for the google project, otherwise you may get a warning as _development purposes only_.

Add a `.env` file or `.env.local` in the project root and specify your API key as `REACT_APP_GOOGLE_MAPS_API_KEY=your_api_key_here`

In the project directory, you can run:

```
yarn install
yarn start
```

OR using npm

```
npm install
npm start
```