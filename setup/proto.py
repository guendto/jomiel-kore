# -*- coding: utf-8 -*-
#
# jomiel-kore
#
# Copyright
#  2019-2020 Toni Gündoğdu
#
#
# SPDX-License-Identifier: Apache-2.0
#
"""TODO."""


def compile_protobuf_bindings(bootstrap_path, proto_dir, dest_dir):
    """Compile the proto buffer declarations.

    This function calls the `bootstrap` script of jomiel-kore to produce
    the bindings.

    Args:
        bootstrap_path (str): the path to the `bootstrap` script

        proto_dir (str): the path to the _root_ dir containing the
            .proto files

        dest_dir (str): the destination dir for the compiled bindings

    """
    from subprocess import call
    from os.path import sep
    from os import EX_OK

    args = [
        bootstrap_path,
        "-p",
        proto_dir,
        "-l",
        "python",
        "-d",
        dest_dir.replace(".", sep),
    ]

    from ..app import exit_error

    if call(args) != EX_OK:
        exit_error()


def generate_protobuf_bindings():
    """Generates the bindings for the protobuf message declarations."""
    from ..app import exit_error

    protoc = detect_protoc()
    if not protoc:
        print("error: protoc command not found")
        exit_error()

    from subprocess import call
    from os import EX_OK

    from .cache import PROTO_FILES, PROTO_PATH
    from .echo import put

    put("Compiling the protobuf declarations for jomiel messages\n")

    for fname in PROTO_FILES:
        put("  Compiling %s..." % fname)
        args = [
            protoc,
            "-I" + PROTO_PATH,
            "--python_out=" + PROTO_PATH,
            fname,
        ]
        if call(args) != EX_OK:
            exit_error()
        put(" done.\n")


def detect_protoc():
    """Try to find the protoc(1) command."""
    from os.path import exists
    from os import environ

    if "PROTOC" in environ and exists(environ["PROTOC"]):
        return environ["PROTOC"]

    from distutils.spawn import find_executable

    return find_executable("protoc")


# vim: set ts=4 sw=4 tw=72 expandtab:
