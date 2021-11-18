from simplecomputingcluster import init_app

app = init_app()


if __name__ == "__main__":
    import argparse
    cli = argparse.ArgumentParser(description="Facade for Pipeator.")
    cli.add_argument("--host", default="0.0.0.0",
                     help="Host in the IPv4 convention.")
    cli.add_argument("--port", default=8957,
                     help="Port to listen to.")
    cli.add_argument("--debug", action="store_true",
                     help="Run in debug mode.")
    cli.add_argument("--notthreaded", action="store_false",
                     help="Run with single thread.")
    args = cli.parse_args()

    app.run(debug=args.debug,
            host=args.host,
            port=args.port,
            threaded=args.notthreaded)
 
