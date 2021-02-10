import numpy as np
import plotly.graph_objects as go


def plot_time_from_first(lap_time_matrix: np.ndarray) -> go.Figure:
    """
    Given a matrix which contains the lap times for each of the drivers, this function
    generate a Plotly figure which plots the gap from first place for each of the
    drivers (in seconds)

    Parameters
    ----------
    lap_time_matrix
        An array where each row contains the lap times for a driver

    Returns
    -------
    go.Figure
        A Plotly figure with the laps on the x-axis and the gap to first place on the
        y-axis
    """
    figure = go.Figure()

    cumulative_lap_time_matrix = np.cumsum(lap_time_matrix, axis=1)
    lowest_total_time_per_lap_matrix = np.min(cumulative_lap_time_matrix, axis=0)
    distance_to_first_matrix = (
        cumulative_lap_time_matrix - lowest_total_time_per_lap_matrix
    )
    generate_line_plots(distance_to_first_matrix, lap_time_matrix, figure)

    figure['layout']['xaxis']['title'] = 'Lap'
    figure['layout']['yaxis']['title'] = 'Gap from first place (in seconds)'
    figure['layout']['title'] = 'Race simulation results'
    figure.show()


def plot_position(lap_time_matrix: np.ndarray):
    """
    Given a matrix which contains the lap times for each of the drivers, this function
    generate a Plotly figure which plots the position of the drivers

    Parameters
    ----------
    lap_time_matrix
        An array where each row contains the lap times for a driver

    Returns
    -------
    go.Figure
        A Plotly figure with the laps on the x-axis and the driver's position on the
        y-axis
    """
    figure = go.Figure()

    cumulative_lap_time_matrix = np.cumsum(lap_time_matrix, axis=1)
    position_matrix = np.argsort(np.argsort(cumulative_lap_time_matrix, axis=0), axis=0)
    generate_line_plots(position_matrix, lap_time_matrix, figure)

    figure['layout']['xaxis']['title'] = 'Lap'
    figure['layout']['yaxis']['title'] = 'Driver position'
    figure.show()


def generate_line_plots(
    y_matrix: np.ndarray,
    lap_time_matrix: np.ndarray,
    figure: go.Figure,
) -> None:
    """
    Given a matrix of lap times and a matrix to plot on the y-axis, this function will
    add line plots to the figure. Each line could represent, e.g., the distance to
    the first driver or the position of the driver

    Parameters
    ----------
    y_matrix
        Each row of this matrix will become a separate line in the figure
    lap_time_matrix
        A matrix with the lap times for each driver
    figure
        The figure to which the lines should be added

    Returns
    -------

    """
    for driver_idx in range(lap_time_matrix.shape[0]):
        line_plot = go.Scatter(
            x=list(range(lap_time_matrix.shape[1])),
            y=y_matrix[driver_idx, :],
            name=f'Driver {driver_idx}',
            marker_size=1,
        )

        figure.add_trace(line_plot)
