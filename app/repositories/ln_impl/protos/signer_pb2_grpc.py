# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import signer_pb2 as signer__pb2


class SignerStub(object):
    """Signer is a service that gives access to the signing functionality of the
    daemon's wallet.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SignOutputRaw = channel.unary_unary(
            '/signrpc.Signer/SignOutputRaw',
            request_serializer=signer__pb2.SignReq.SerializeToString,
            response_deserializer=signer__pb2.SignResp.FromString,
        )
        self.ComputeInputScript = channel.unary_unary(
            '/signrpc.Signer/ComputeInputScript',
            request_serializer=signer__pb2.SignReq.SerializeToString,
            response_deserializer=signer__pb2.InputScriptResp.FromString,
        )
        self.SignMessage = channel.unary_unary(
            '/signrpc.Signer/SignMessage',
            request_serializer=signer__pb2.SignMessageReq.SerializeToString,
            response_deserializer=signer__pb2.SignMessageResp.FromString,
        )
        self.VerifyMessage = channel.unary_unary(
            '/signrpc.Signer/VerifyMessage',
            request_serializer=signer__pb2.VerifyMessageReq.SerializeToString,
            response_deserializer=signer__pb2.VerifyMessageResp.FromString,
        )
        self.DeriveSharedKey = channel.unary_unary(
            '/signrpc.Signer/DeriveSharedKey',
            request_serializer=signer__pb2.SharedKeyRequest.SerializeToString,
            response_deserializer=signer__pb2.SharedKeyResponse.FromString,
        )


class SignerServicer(object):
    """Signer is a service that gives access to the signing functionality of the
    daemon's wallet.
    """

    def SignOutputRaw(self, request, context):
        """
        SignOutputRaw is a method that can be used to generated a signature for a
        set of inputs/outputs to a transaction. Each request specifies details
        concerning how the outputs should be signed, which keys they should be
        signed with, and also any optional tweaks. The return value is a fixed
        64-byte signature (the same format as we use on the wire in Lightning).

        If we are  unable to sign using the specified keys, then an error will be
        returned.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ComputeInputScript(self, request, context):
        """
        ComputeInputScript generates a complete InputIndex for the passed
        transaction with the signature as defined within the passed SignDescriptor.
        This method should be capable of generating the proper input script for
        both regular p2wkh output and p2wkh outputs nested within a regular p2sh
        output.

        Note that when using this method to sign inputs belonging to the wallet,
        the only items of the SignDescriptor that need to be populated are pkScript
        in the TxOut field, the value in that same field, and finally the input
        index.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SignMessage(self, request, context):
        """
        SignMessage signs a message with the key specified in the key locator. The
        returned signature is fixed-size LN wire format encoded.

        The main difference to SignMessage in the main RPC is that a specific key is
        used to sign the message instead of the node identity private key.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def VerifyMessage(self, request, context):
        """
        VerifyMessage verifies a signature over a message using the public key
        provided. The signature must be fixed-size LN wire format encoded.

        The main difference to VerifyMessage in the main RPC is that the public key
        used to sign the message does not have to be a node known to the network.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeriveSharedKey(self, request, context):
        """
        DeriveSharedKey returns a shared secret key by performing Diffie-Hellman key
        derivation between the ephemeral public key in the request and the node's
        key specified in the key_desc parameter. Either a key locator or a raw
        public key is expected in the key_desc, if neither is supplied, defaults to
        the node's identity private key:
        P_shared = privKeyNode * ephemeralPubkey
        The resulting shared public key is serialized in the compressed format and
        hashed with sha256, resulting in the final key length of 256bit.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SignerServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'SignOutputRaw': grpc.unary_unary_rpc_method_handler(
            servicer.SignOutputRaw,
            request_deserializer=signer__pb2.SignReq.FromString,
            response_serializer=signer__pb2.SignResp.SerializeToString,
        ),
        'ComputeInputScript': grpc.unary_unary_rpc_method_handler(
            servicer.ComputeInputScript,
            request_deserializer=signer__pb2.SignReq.FromString,
            response_serializer=signer__pb2.InputScriptResp.SerializeToString,
        ),
        'SignMessage': grpc.unary_unary_rpc_method_handler(
            servicer.SignMessage,
            request_deserializer=signer__pb2.SignMessageReq.FromString,
            response_serializer=signer__pb2.SignMessageResp.SerializeToString,
        ),
        'VerifyMessage': grpc.unary_unary_rpc_method_handler(
            servicer.VerifyMessage,
            request_deserializer=signer__pb2.VerifyMessageReq.FromString,
            response_serializer=signer__pb2.VerifyMessageResp.SerializeToString,
        ),
        'DeriveSharedKey': grpc.unary_unary_rpc_method_handler(
            servicer.DeriveSharedKey,
            request_deserializer=signer__pb2.SharedKeyRequest.FromString,
            response_serializer=signer__pb2.SharedKeyResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'signrpc.Signer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

 # This class is part of an EXPERIMENTAL API.


class Signer(object):
    """Signer is a service that gives access to the signing functionality of the
    daemon's wallet.
    """

    @staticmethod
    def SignOutputRaw(request,
                      target,
                      options=(),
                      channel_credentials=None,
                      call_credentials=None,
                      insecure=False,
                      compression=None,
                      wait_for_ready=None,
                      timeout=None,
                      metadata=None):
        return grpc.experimental.unary_unary(request, target, '/signrpc.Signer/SignOutputRaw',
                                             signer__pb2.SignReq.SerializeToString,
                                             signer__pb2.SignResp.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ComputeInputScript(request,
                           target,
                           options=(),
                           channel_credentials=None,
                           call_credentials=None,
                           insecure=False,
                           compression=None,
                           wait_for_ready=None,
                           timeout=None,
                           metadata=None):
        return grpc.experimental.unary_unary(request, target, '/signrpc.Signer/ComputeInputScript',
                                             signer__pb2.SignReq.SerializeToString,
                                             signer__pb2.InputScriptResp.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SignMessage(request,
                    target,
                    options=(),
                    channel_credentials=None,
                    call_credentials=None,
                    insecure=False,
                    compression=None,
                    wait_for_ready=None,
                    timeout=None,
                    metadata=None):
        return grpc.experimental.unary_unary(request, target, '/signrpc.Signer/SignMessage',
                                             signer__pb2.SignMessageReq.SerializeToString,
                                             signer__pb2.SignMessageResp.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def VerifyMessage(request,
                      target,
                      options=(),
                      channel_credentials=None,
                      call_credentials=None,
                      insecure=False,
                      compression=None,
                      wait_for_ready=None,
                      timeout=None,
                      metadata=None):
        return grpc.experimental.unary_unary(request, target, '/signrpc.Signer/VerifyMessage',
                                             signer__pb2.VerifyMessageReq.SerializeToString,
                                             signer__pb2.VerifyMessageResp.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeriveSharedKey(request,
                        target,
                        options=(),
                        channel_credentials=None,
                        call_credentials=None,
                        insecure=False,
                        compression=None,
                        wait_for_ready=None,
                        timeout=None,
                        metadata=None):
        return grpc.experimental.unary_unary(request, target, '/signrpc.Signer/DeriveSharedKey',
                                             signer__pb2.SharedKeyRequest.SerializeToString,
                                             signer__pb2.SharedKeyResponse.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
