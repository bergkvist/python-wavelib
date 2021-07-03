#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
namespace py = pybind11;

py::array edge_trigger(py::array_t<double> input, double cursor, double noise_threshold) {
    auto input_data = input.unchecked<1>();
    auto result = py::array_t<bool>(input.size());
    auto result_data = result.mutable_data();

    bool has_triggered = input_data[0] < cursor;
    for (py::ssize_t i = 0; i < input.size() - 1; i++) {
        if (input_data[i] > cursor && input_data[i+1] <= cursor && !has_triggered) {
            has_triggered = true;
            result_data[i] = 1;
        } else {
            result_data[i] = 0;
        }

        if (input_data[i] > cursor + noise_threshold) {
            has_triggered = false;
        }
    }
    result_data[input.size() - 1] = 0;

    return std::move(result);
}

py::array trigger_count(py::array_t<bool> trigger) {
    auto trigger_data = trigger.unchecked<1>();
    auto result = py::array_t<double>(trigger.size());
    auto result_data = result.mutable_data();

    py::ssize_t j = 0;
    py::ssize_t n = 0;
    py::ssize_t i = 0;
    for (i = 0; i < trigger.size(); ++i) {
        if (trigger_data[i]) {
            for (py::ssize_t k = i-1; k >= j; k--) {
                result_data[k] = n + double(k - j) / (i - j);
            }
            j = i;
            n++;
        }
    }
    for (py::ssize_t k = i-1; k >= j; k--) {
        result_data[k] = n + double(k - j) / (i - j);
    }
    return std::move(result);
}

PYBIND11_MODULE(wavelib, m) {
    m.doc() = "Signal processing utilities for Python/Numpy written in C++";
    m.def("edge_trigger", edge_trigger, 
        py::arg("input"),
        py::arg("cursor") = double(0),
        py::arg("noise_threshold") = double(0),
        "Detect when a signal passes down through a cursor - but only after first having been above a noise threshold."
    );
    m.def("trigger_count", trigger_count, py::arg("trigger"), "Linearly interpolated number of triggers that has happened so far");
}